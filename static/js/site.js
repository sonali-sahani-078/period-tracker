document.addEventListener("DOMContentLoaded", () => {
  const revealEls = document.querySelectorAll(".reveal");
  const nav = document.querySelector(".app-nav");

  revealEls.forEach((el, index) => {
    el.style.setProperty("--reveal-delay", `${Math.min(index * 70, 280)}ms`);
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2, rootMargin: "0px 0px -40px 0px" }
  );

  revealEls.forEach((el) => observer.observe(el));

  const syncNavState = () => {
    if (!nav) return;
    nav.classList.toggle("nav-scrolled", window.scrollY > 10);
  };

  syncNavState();
  window.addEventListener("scroll", syncNavState, { passive: true });
});
