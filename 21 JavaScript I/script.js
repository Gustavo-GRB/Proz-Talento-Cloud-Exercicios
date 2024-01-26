let titulo = document.createElement("h1");

titulo.id = "titulo";
titulo.innerText = "Pet Shop";

let body = document.querySelector("body");

body.appendChild(titulo);

let produto = document.createElement("div");

produto.innerHTML = `
  <div>
    <h2>banho e tosa</h2>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIRNnzatLha6reKEVqlfvI_hmD1ayQVdxE4A&usqp=CAU" alt="banho e tosa">
    <p>Banho, Secagem, Limpeza de ouvidos e olhos, Corte de unhas, Tosa da pelagem</p>
    <p id="preco-banho-tosa"> R$ 60.00</p>
  </div>
`

body.appendChild(produto)