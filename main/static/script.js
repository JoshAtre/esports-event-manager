// counter to track current month
let monthOffset = 0;

// track what day user clicks on
let dayClicked = null;

// either an empty array or the array of event objects
let events = localStorage.getItem('events') ? JSON.parse(localStorage.getItem('events')) : [];

const calendar = document.getElementById('calendar');
const weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
const newEventModal = document.getElementById('newEventModal');
const deleteEventModal = document.getElementById('deleteEventModal');
const backDrop = document.getElementById('modalBackDrop');
const eventTitleInput = document.getElementById('eventTitleInput');

// function to loadCal the calendar
function loadCal() {
    const dt = new Date();

    // set the proper month based on which button(s) the user presses
    if (monthOffset !== 0) {
        dt.setMonth(new Date().getMonth() + monthOffset);
    }

    const day = dt.getDate();
    const month = dt.getMonth();
    const year = dt.getFullYear();

    const firstDayOfMonth = new Date(year, month, 1);

    // number representing days in the current month
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const dateString = firstDayOfMonth.toLocaleDateString('en-us', {
        weekday: 'long',
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
    });

    // determines how many padding days needed at the beginning of the month
    const padDays = weekdays.indexOf(dateString.split(', ')[0]);

    // use dt and string interpolation to display the name of the current month
    document.getElementById('monthDisplay').innerText = 
        `${dt.toLocaleDateString('en-us', {month: 'long'})} ${year}`;

    // reset the calendar before rendering squares
    calendar.innerHTML = '';

    // render the squares for the days of the month
    for(let i = 1; i <= padDays + daysInMonth; ++i) {
        const daySquare = document.createElement('div');
        daySquare.classList.add('day');

        const dayString = `${month + 1}/${i - padDays}/${year}`;

        // true if padding days are done rendering
        if (i > padDays) {
            daySquare.innerText = i - padDays;

            const eventForDay = events.find(e => e.date === dayString);

            // if rendered square is the current day, highlight it
            if (i - padDays === day && monthOffset === 0) {
                daySquare.id = 'currentDay';
            }

            // if an event exists for the given day, display it on the
            // day square
            if (eventForDay) {
                const eventDiv = document.createElement('div');
                eventDiv.classList.add('event');
                eventDiv.innerText = eventForDay.title;
                daySquare.appendChild(eventDiv);
            }

            // if a day square is dayClicked, open the modal
            daySquare.addEventListener('click', () => openModal(dayString));
        }
        // adds padding days
        else {
            daySquare.classList.add('padding');
        }

        calendar.appendChild(daySquare);
    }
}

function saveEvent() {
    // if event title input is not null, remove errors
    if (eventTitleInput.value) {
        eventTitleInput.classList.remove('error');

        events.push({
            date: dayClicked,
            title: eventTitleInput.value,
        });
        
        // save the events array to localStorage after pushing
        // the event onto the array
        localStorage.setItem('events', JSON.stringify(events))
        closeModal();
    }
    else {
        eventTitleInput.classList.add('error');
    }
}

function deleteEvent() {
    // reset the events array to include all events except
    // for the event to be deleted
    events = events.filter(e => e.date !== dayClicked);
    localStorage.setItem('events', JSON.stringify(events));
    closeModal();
}

// function to handle the display of modals
function openModal(date) {
    dayClicked = date;

    // check to see if event exists for the given date
    const eventForDay = events.find(e => e.date === dayClicked);

    if (eventForDay) {
        document.getElementById('eventText').innerText = eventForDay.title;
        deleteEventModal.style.display = 'block';
    }
    else {
        newEventModal.style.display = 'block';

    }

    backDrop.style.display = 'block';
}

function closeModal() {
    // clear the modal
    eventTitleInput.classList.remove('error');
    newEventModal.style.display = 'none';
    deleteEventModal.style.display = 'none';
    backDrop.style.display = 'none';
    eventTitleInput.value = '';
    dayClicked = null;
    loadCal();

}

// add functionality to the buttons, reloadCal the calendar after each click
function initButtons() {
    document.getElementById('nextButton').addEventListener('click', () => {
        monthOffset++;
        loadCal();
    });

    document.getElementById('backButton').addEventListener('click', () => {
        monthOffset--;
        loadCal();
    });

    document.getElementById('saveButton').addEventListener('click', saveEvent);
    document.getElementById('cancelButton').addEventListener('click', closeModal);

    document.getElementById('deleteButton').addEventListener('click', deleteEvent);
    document.getElementById('closeButton').addEventListener('click', closeModal);

}

initButtons();
loadCal();