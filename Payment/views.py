import logging
from Store .models import Order
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.contrib import messages
from django.db.models import Sum
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def go_to_gateway_view(request):
    if request.user.is_authenticated == True and request.user.registered == True:
        if request.user.shopping_cart.exists():

            if request.user.check_address() and request.user.check_address():
                user = request.user
                # مقداد مالیات
                tax_rate = 0.09
                # محاصبه مالیات
                total_price_with_tax = user.shopping_cart.aggregate(total_price=Sum('price'))['total_price'] * tax_rate
                # جمع کل 
                total_price = user.shopping_cart.aggregate(total_price=Sum('price'))[
                                  'total_price'] + total_price_with_tax

                amount = total_price
                # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
                user_mobile_number = str(user.phone_number)  # اختیاری

                factory = bankfactories.BankFactory()

                try:
                    bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
                    bank.set_request(request)
                    bank.set_amount(amount)
                    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
                    bank.set_client_callback_url(reverse('callback-gateway'))
                    bank.set_mobile_number(user_mobile_number)  # اختیاری

                    # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
                    # پرداخت برقرار کنید.
                    bank_record = bank.ready()

                    # هدایت کاربر به درگاه بانک
                    return bank.redirect_gateway()

                except AZBankGatewaysException as Erorr:
                    return Erorr



            else:
                messages.success(request, 'اطلاعات شما برای ادامه خرید ناقص است لطفا اطلاعات خود را تکمیل کنید')
                return HttpResponseRedirect(reverse('Account:edit_profile'))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        user = request.user
        total_price = user.shopping_cart.all().aggregate(Sum('price'))
        user_address = f' کدپستی : {user.main_address.post_code}  واحد: {user.main_address.home_unit}  پلاک: {user.main_address.house_number} آدرس: {user.main_address.address} استان: {user.main_address.provinec}'
        order = Order.objects.create(
            user=user, status='aw', total_price=total_price['price__sum'], address=user_address)

        for item in user.shopping_cart.all():
            order.products.add(item)
            item.quantity -= 1
            item.save()

        user.shopping_cart.clear()
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."
    )
