const formula_container = document.querySelectorAll(".formula_container");

formula_container.forEach((element) => {
  let tab_opened = false;
  element.firstElementChild.addEventListener("click", () => {
    if (tab_opened) {
      element.lastElementChild.classList.remove("open");
      element.firstElementChild.classList.remove("open_");
      tab_opened = false;
    } else {
      element.lastElementChild.classList.add("open");
      element.firstElementChild.classList.add("open_");
      tab_opened = true;
    }
  });
});
