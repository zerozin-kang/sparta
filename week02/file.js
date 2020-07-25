let fruitsBasket = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

let count = 0;
for (let i = 0; i < fruitsBasket.length; i++) {
	let fruit = fruitsBasket[i];
	if (fruit == '딸기') {
		count += 1;
	}
}
console.log(count);