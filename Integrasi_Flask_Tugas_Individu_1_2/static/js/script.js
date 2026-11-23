document.addEventListener("DOMContentLoaded", () => {
  // Menandai menu navigasi sesuai halaman yang sedang dibuka.
  const currentPath = window.location.pathname;
  document.querySelectorAll(".navbar .nav-link").forEach((link) => {
    const linkPath = new URL(link.href).pathname;
    link.classList.toggle("active", linkPath === currentPath);
  });
});
