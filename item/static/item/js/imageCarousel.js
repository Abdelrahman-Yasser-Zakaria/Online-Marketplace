document.addEventListener("DOMContentLoaded", function () {
  const images = document.querySelectorAll("[data-slide]"); // how to send these images list to separate js file
  const dots = document.querySelectorAll("[data-slide-to]");
  const prevBtn = document.querySelector(".absolute.left-4");
  const nextBtn = document.querySelector(".absolute.right-4");
  const counter = document.getElementById("current-image");
  let currentSlide = 0;

  function showSlide(n) {
    // Show image slide by passing slide index
    images.forEach((img) => img.classList.add("hidden")); // hide all image slides
    dots.forEach((dot) => dot.classList.remove("bg-opacity-100")); // remove active state from all dots

    if (n >= images.length) n = 0;
    if (n < 0) n = images.length - 1;
    currentSlide = n;

    images[currentSlide].classList.remove("hidden"); // show the image of current slide only
    dots[currentSlide].classList.add("bg-opacity-100"); // show active state dot for the current slide only
    counter.textContent = currentSlide + 1;
  }

  nextBtn.addEventListener("click", () => {
    currentSlide++;
    showSlide(currentSlide);
  });

  prevBtn.addEventListener("click", () => {
    currentSlide--;
    showSlide(currentSlide);
  });

  dots.forEach((dot, index) => {
    dot.addEventListener("click", () => {
      currentSlide = index;
      showSlide(currentSlide);
    });
  });
});
