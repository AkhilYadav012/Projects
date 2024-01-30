let currentIndex = 0;

  function showSlide(index) {
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;
    currentIndex = (index + totalSlides) % totalSlides;

    const translateValue = -currentIndex * 100;
    slides.style.transform = `translateX(${translateValue}%)`;
  }

  function prevSlide() {
    showSlide(currentIndex - 1);
  }

  function nextSlide() {
    showSlide(currentIndex + 1);
  }

  setInterval(nextSlide, 3000); 

  function search() {
    const searchTerm = document.getElementById('search-box').value;

   
    alert(`Searching for: ${searchTerm}`);
  }