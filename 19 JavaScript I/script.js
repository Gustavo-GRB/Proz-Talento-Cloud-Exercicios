let elementoH1 = document.querySelector("h1");
console.log(elementoH1);

let elementoA = document.querySelector("a");
console.log(elementoA);

let elementoUl = document.querySelector("ul");
console.log(elementoUl);

let elementoOl = document.querySelector("ol");
console.log(elementoOl);


let elementoMain = document.querySelector("main");

elementoMain.innerHTML = `
<h1 id="titulo">Título</h1>
<ul>
    <li>Google</li>
    <li>Microsoft</li>
    <li>Apple</li>
</ul>
<a href="https://prozeducacao.com.br">Proz</a>
<ol id="lista-ordenada">
    <li>https://www.google.com.br</li>
    <li>https://www.microsoft.com/pt-br</li>
    <li>https://www.apple.com/br</li>
</ol>

`


