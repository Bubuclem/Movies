const sliderUI = {
    slider: document.getElementById("slider"),
    slides: document.querySelectorAll(".slide"),
    controls: {
      prevBtn: document.getElementById("btn-prev"),
      nextBtn: document.getElementById("btn-next")
    }
  };
  
  let sliderController = {
    isMouseDown: false,
    startPosX: 0,
    scrollLeft: sliderUI.slider.offsetLeft,
    goNext() {
      let _scrollBy = Math.round((sliderUI.slider.offsetWidth + 20) - (sliderUI.slider.scrollLeft % (sliderUI.slides[0].offsetWidth + 20)));
      
      easyScroll({
        scrollableDomEle: sliderUI.slider,
        direction: "right",
        duration: 200,
        easingPreset: "easeInQuad",
        scrollAmount: _scrollBy
      });
    },
    goPrev() {
      let _scrollBy = Math.round(sliderUI.slider.offsetWidth + 20) - (Math.round((sliderUI.slides[0].offsetWidth + 20)) - (sliderUI.slider.scrollLeft % (Math.round(sliderUI.slides[0].offsetWidth + 20))));
      
      easyScroll({
        scrollableDomEle: sliderUI.slider,
        direction: "left",
        duration: 200,
        easingPreset: "easeInQuad",
        scrollAmount: _scrollBy
      });
    }
  };
  
  sliderUI.controls.nextBtn.addEventListener("click", (event) => {
    event.preventDefault();
    sliderController.goNext();
  });
  
  sliderUI.controls.prevBtn.addEventListener("click", (event) => {
    event.preventDefault();
    sliderController.goPrev();
  });
  
  sliderUI.slider.addEventListener("wheel", (event) => {
    event.stopPropagation();
    sliderUI.slider.scrollLeft -= event.wheelDeltaX;
  });
  
  sliderUI.slider.addEventListener("scroll", (event) => {
    if (
      sliderUI.slider.offsetWidth + sliderUI.slider.scrollLeft + 1 >
      sliderUI.slider.scrollWidth
    ) {
      sliderUI.controls.nextBtn.classList.add("hide");
      if (document.activeElement.id === sliderUI.controls.nextBtn.id) {
        sliderUI.controls.prevBtn.focus();
      }
    } else {
      sliderUI.controls.nextBtn.classList.remove("hide");
    }
  
    if (sliderUI.slider.scrollLeft - 1 < 0) {
      sliderUI.controls.prevBtn.classList.add("hide");
      if (document.activeElement.id === sliderUI.controls.prevBtn.id) {
        sliderUI.controls.nextBtn.focus();
      }
    } else {
      sliderUI.controls.prevBtn.classList.remove("hide");
    }
  });
  
  sliderUI.slider.addEventListener("mousedown", (event) => {
    sliderController.isMouseDown = true;
    sliderController.scrollLeft = sliderUI.slider.scrollLeft;
    sliderController.startPosX = event.pageX - sliderUI.slider.offsetLeft;
  });
  
  sliderUI.slider.addEventListener("mousemove", (event) => {
    if (!sliderController.isMouseDown) return;
    let _x = event.pageX - sliderUI.slider.offsetLeft;
    let _xChange = _x - sliderController.startPosX;
    sliderUI.slider.scrollLeft = sliderController.scrollLeft - _xChange;
  });
  
  sliderUI.slider.addEventListener("mouseup", (event) => {
    sliderController.isMouseDown = false;
  });
  
  sliderUI.slider.addEventListener("mouseleave", (event) => {
    sliderController.isMouseDown = false;
  });
  
  sliderUI.slider.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
      sliderController.goPrev();
    }
    if (event.key === "ArrowRight") {
      sliderController.goNext();
    }
  });
  
  sliderUI.slider.addEventListener("touchstart", (event) => {
    sliderController.isMouseDown = true;
    sliderController.scrollLeft = sliderUI.slider.scrollLeft;
    sliderController.startPosX = event.pageX - sliderUI.slider.offsetLeft;
  });
  
  let images = [
  ];
  
  sliderUI.slides.forEach((slide, index) => {
    let img = new Image();
    img.onload = (a) => {
      slide.style.backgroundImage = `url(${images[index]})`;
      slide.classList.add('has-image');
    }
    img.src = images[index];
  });