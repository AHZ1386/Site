'strict mode'

const initSlider = () => {
    const imageList = document.querySelector('.slider-wrapper .image-list');
    const slideButtons = document.querySelectorAll('.slider-wrapper .slide-button');
    const sliderScrollBar  = document.querySelector('.container .slider-scrollbar');
    const scrollBarThumb  = sliderScrollBar.querySelector('.container .scrollbar-thumb');
    const maxScrollLeft = imageList.scrollWidth - imageList.clientWidth;

    scrollBarThumb.addEventListener('mousedown', (e) => {
        const startX = e.clientX;
        const thumbPosition = scrollBarThumb.offsetLeft;

        const handleMouseMove = (e) => {
            const deltaX = e.clientX - startX;
            const newthumbPosition = thumbPosition + deltaX;
            const maxThumbPosition = sliderScrollBar.getBoundingClientRect().width - scrollBarThumb.offsetWidth;

            const boundedPosition = Math.max(0, Math.min(maxThumbPosition,newthumbPosition));
            const scrollPosition = (boundedPosition / maxThumbPosition) * maxScrollLeft;
            console.log(boundedPosition);
            console.log(scrollPosition);
            scrollBarThumb.style.left = `${boundedPosition}px`;
            imageList.scrollLeft = scrollPosition ;
        }
        const handleMouseUp = () => {
            
        document.removeEventListener("mousemove", handleMouseMove);
        document.removeEventListener("mouseup", handleMouseUp);
        }

        document.addEventListener("mousemove", handleMouseMove);
        document.addEventListener("mouseup", handleMouseUp);
    })
    slideButtons.forEach(button => {
        button.addEventListener('click', () => {
            const direction = button.id === 'prev-slide' ? -1 : 1;
            const scrollAmount = imageList.clientWidth * direction;
            imageList.scrollBy({ left: scrollAmount, behavior: 'smooth'});
        })
    });

    const handleSliderButtons = () => {
            slideButtons[0].style.display = imageList.scrollLeft <= 0 ? 'none' : 'block';
            slideButtons[1].style.display = imageList.scrollLeft >= maxScrollLeft ? 'none' : 'block';
            console.log(imageList.scrollLeft);
    }

    const updateScrollThumbPosition = () => {
        const scrollPosition = imageList.scrollLeft;
        const thumbPosition = (scrollPosition / maxScrollLeft) * (sliderScrollBar.clientWidth - scrollBarThumb.offsetWidth);
        scrollBarThumb.style.left = `${thumbPosition}px`
        // console.log(scrollPosition, thumbPosition);
    }

    imageList.addEventListener('scroll' ,() => {
        handleSliderButtons();
        updateScrollThumbPosition();
})
}

window.addEventListener('load', initSlider);