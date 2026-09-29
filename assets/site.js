/* Progressive enhancement. No tracking, inventory requests, or visitor storage. */
document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = String(new Date().getFullYear());
});
const menu = document.querySelector(".mobile-menu");
if (menu) {
  menu.querySelectorAll("a").forEach((link) =>
    link.addEventListener("click", () => {
      menu.open = false;
    }),
  );
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menu.open) {
      menu.open = false;
      menu.querySelector("summary").focus();
    }
  });
}
const search = document.querySelector("#archive-search");
if (search) {
  const cards = [...document.querySelectorAll(".directory-card")];
  const status = document.querySelector("#result-count");
  const empty = document.querySelector("#no-results");
  const filter = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    cards.forEach((card) => {
      const matches = card.textContent.toLocaleLowerCase().includes(query);
      card.hidden = !matches;
      if (matches) count++;
    });
    status.textContent = `${count} ${count === 1 ? "category" : "categories"}`;
    empty.hidden = count !== 0;
  };
  document.querySelector(".archive-tools").hidden = false;
  search.addEventListener("input", filter);
  document.querySelector("#clear-search").addEventListener("click", () => {
    search.value = "";
    filter();
    search.focus();
  });
  filter();
}
