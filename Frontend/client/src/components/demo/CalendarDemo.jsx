import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useState } from "react";

export function CalendarDemo({ onDateChange }) {
  const [selectedDate, setSelectedDate] = useState(null);

  const handleChange = (date) => {
    const dateValue = date;
    const day = dateValue.getDate();
    const month = dateValue.getMonth() + 1;
    const year = dateValue.getFullYear();
    const formattedDate = `${day.toString().padStart(2, "0")}-${month
      .toString()
      .padStart(2, "0")}-${year}`;
    setSelectedDate(date);
    onDateChange(formattedDate);
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
