import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useState } from "react";

export function CalendarDemo({ onDateChange }) {
  const [selectedDate, setSelectedDate] = useState(null);

  const handleChange = (date) => {
    const dateValue = date;
    const day = dateValue.getDate(); // Day of the month (1-31)
    const month = dateValue.getMonth() + 1; // Months are zero-indexed (0-11), so add 1 to get 1-12
    const year = dateValue.getFullYear(); // Full year (e.g., 2024)
    const formattedDate = `${day.toString().padStart(2, "0")}-${month
      .toString()
      .padStart(2, "0")}-${year}`;
    setSelectedDate(date);
    onDateChange(formattedDate); // Pass the selected date to the parent component
  };

  return (
    <>
      <DatePicker
        selected={selectedDate}
        label="Calendar"
        className="border border-gray-800 rounded-2xl text-md pl-4 text-black outline-none py-1"
        onChange={handleChange}
      />
    </>
  );
}
