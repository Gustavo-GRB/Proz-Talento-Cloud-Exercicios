let numerosDaSorte = [37, 14, 26, 5, 94, 87];

for (i=0; i<numerosDaSorte.length; i++) {
    let numSorte = numerosDaSorte[i];
    if (numSorte % 2 === 0 && numSorte < 50){
        console.log(`${numSorte} é par e menor que 50`);
    }else if(numSorte < 50){
        console.log(`${numSorte} é menor que 50`);
    }else
        console.log(`${numSorte} é maior que 50`);
}
