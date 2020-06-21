const date = new Date();

myModalImage=document.querySelector("#mymodal img");
myModalBody=document.querySelector("#myModal h3");

const renderCalendar = () => {
  date.setDate(1);

  const listEvents=
{
	"January": {
		"16": ["Birthday", "Seema Sinha"],
		"25": ["Anniversary", "Seema Sinha","Prabhat Kumar"]
	},
	"February": {
		"22": ["Birthday","Prateek Sinha"]
	},
	"March": {
	  "14":["Birthday","Ajay Kumar Sinha"]
    },
	"April": {
		"30": ["Birthday","Sweta Kumari"]
	},
	"May": {
        "17":["Birthday","Pradeep Kumar"]
	},
    "June": {
	  "10":["Birthday","Abha Sinha"],
      "18":["Anniversary","Lalita Sinha","P. N. Sinha"],
      "27":["Anniversary","Jyoti Sinha","Ajay kumar Sinha"]
    },
    "August":{
	  "10":["Birthday","Sachin Sinha"]
    },
    "September":{
	  "26":["Birthday","Runnu Sinha"],
	  "28":["Birthday","Prabhat Kumar","Pratyaksha Sinha"]
    },
    "October":{
	  "2":["Birthday","Pranay Sinha"],
      "13":["Birthday","P. N. Sinha"]
    },
    "November":{
	  "4":["Birthday","Prajjwal Sinha"],
      "22":["Anniversary","Abha Sinha","Pradeep Kumar"],
      "23":["Birthday","Lalita Sinha"],
      "28":["Anniversary","Sweta Kumari","Pravin Kumar"]
    },
    "December":{
	  "10":["Birthday","Jyoti Sinha"],
      "1":["Birthday","Pranav Sinha"],
      "25":["Birthday","Bhavya Sinha"],
      "26":["Birthday","Pravin Kumar"]
    }
};


  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  const nextDays = 7 - lastDayIndex - 1;

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  document.querySelector(".date h1").innerHTML = months[date.getMonth()];

  document.querySelector(".date p").innerHTML = date.getFullYear();

  let days = "";

  for (let x = firstDayIndex; x > 0; x--) {
    days += `<div class="prev-date">${prevLastDay - x +1}</div>`;
  }

  for (let i = 1; i <= lastDay; i++) {
    if (listEvents.hasOwnProperty(months[date.getMonth()]) && listEvents[months[date.getMonth()]].hasOwnProperty(i)){
      var thisMonthEvents=listEvents[months[date.getMonth()]];
        if(thisMonthEvents[i][0]==="Birthday" && i === new Date().getDate() &&
      date.getMonth() === new Date().getMonth() &&
      date.getFullYear() === new Date().getFullYear()){
          days+=`<div class="today"><i class="fas fa-birthday-cake" style="color: #CBAB1A"></i><br>${i}</div>`
        }
        else if (thisMonthEvents[i][0]==="Anniversary" && i === new Date().getDate() &&
      date.getMonth() === new Date().getMonth() &&
      date.getFullYear() === new Date().getFullYear()){
          days+=`<div class="today"><i class="fas fa-heart" style="color:red;"></i><br>${i}</div>`
        }
        else if(thisMonthEvents[i][0]==="Birthday"){
          days+=`<div class="normal-dates"><i class="fas fa-birthday-cake" style="color: #CBAB1A"></i><br>${i}</div>`
        }
        else if (thisMonthEvents[i][0]==="Anniversary"){
          days+=`<div class="normal-dates"><i class="fas fa-heart" style="color:red;"></i><br>${i}</div>`
        }
    }
    else if (
      i === new Date().getDate() &&
      date.getMonth() === new Date().getMonth() &&
      date.getFullYear() === new Date().getFullYear()
    ) {
      days += `<div class="today">${i}</div>`;
    } else {
      days += `<div class="normal-dates">${i}</div>`;
    }
  }

  for (let j = 1; j <= nextDays; j++) {
    days += `<div class="next-date">${j}</div>`;
  }
  monthDays.innerHTML = days;

  document.querySelectorAll(".normal-dates, .today").forEach(item => {
  item.addEventListener("click", event => {
    myModalBody.innerHTML="No Events on this date.";
    var targetDate=new Date();
    targetDate.setDate(event.target.textContent);
    targetDate.setMonth(date.getMonth());
    targetDate.setFullYear(date.getFullYear());
    if (listEvents.hasOwnProperty(months[targetDate.getMonth()])){
      var eventsThisMonth=listEvents[(months[targetDate.getMonth()])];
      if (eventsThisMonth.hasOwnProperty(targetDate.getDate())){
        if (eventsThisMonth[targetDate.getDate()].length === 3){
          myModalBody.innerHTML=eventsThisMonth[targetDate.getDate()][0]+" of "+
              eventsThisMonth[targetDate.getDate()][1]+" and "+eventsThisMonth[targetDate.getDate()][2];
        }
        else {
          myModalBody.innerHTML=eventsThisMonth[targetDate.getDate()][0] + " of " + eventsThisMonth[targetDate.getDate()][1];
        }
        }
    }
    $('#myModal').modal('show');
  })
});
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();

