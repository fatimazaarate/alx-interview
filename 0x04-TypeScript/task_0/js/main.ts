interface Student{
	firstName: string;
	lastName: string;
	age: number;
	location: string;
}
const studentOne: Student = {
	firstName: 'Hafsa',
	lastName: 'Chenni',
	age: 21,
	location: 'planet earth',
};

const studentTwo: Student = {
	firstName: 'Alex',
        lastName: 'Smith',
        age: 21,
        location: 'planet earth',
};
const studentsList: Student[] = [studentOne, studentTwo];

const table = document.createElement('table');
const tbody = document.createElement('tbody');

studentsList.forEach(student => {
	const row = document.createElement("tr");
	const cellName = document.createElement("td");
	const locationName = document.createElement("td");

	cellName.textContent = student.firstName;
	locationName.textContent = student.location;
	row.appendChild(cellName);
	row.appendChild(locationName);
	tbody.appendChild(row);
});
table.appendChild(tbody);
document.body.appendChild(table);
