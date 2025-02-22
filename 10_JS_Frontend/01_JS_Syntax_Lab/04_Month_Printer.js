function monthPrinter (month) {

    let months = ["January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ];

    if (month < 1 || month > 12) {
        console.log('Error!');
    }else{
        console.log(months[month - 1])
    }

}


monthPrinter(13)