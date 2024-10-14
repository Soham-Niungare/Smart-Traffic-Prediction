import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useState } from "react";


export function CalendarDemo() {
  const [selectedDate, setSelectedDate] = useState(null);
  return (
    <>
      <DatePicker
        selected={selectedDate}
        onChange={(date) => setSelectedDate(date)}
        label="Basic date picker"
      />
    </>
  );
}
