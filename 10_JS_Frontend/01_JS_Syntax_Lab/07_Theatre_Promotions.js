function solve (day, age){

    let price;

    if (age >= 0 && age <= 18){
        if (day == 'Weekday'){
        price = 12
        }
        else if (day == 'Weekend'){
            price= 15
        }

        else {
            price = 5
        }
    }

    else  if (age > 18 && age <= 64){
        if (day == 'Weekday'){
        price = 18
        }
        else if (day == 'Weekend'){
            price= 20
        }

        else {
            price = 12
        }
    }

    else  if (age > 64 && age <= 122){
        if (day == 'Weekday'){
        price = 12
        }
        else if (day == 'Weekend'){
            price= 15
        }

        else {
            price = 10
        }
    }
        
    if (price) {
        console.log(`${price}$`)
    }
    else{
        console.log("Error!")
    }
    
}

solve('Weekday', 
42
)

solve('Holiday', -12)

solve('Holiday', 15)