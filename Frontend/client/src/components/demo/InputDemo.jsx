import { Input } from "@/components/ui/input";
import { DropdownMenuLoc } from "./DropdownLoc";
import { CalendarDemo } from "./CalendarDemo";
import { Button } from "../ui/button";
import { useState } from "react";

export function InputDemo(props) {
  const [selectedDate, setSelectedDate] = useState(null);
  const [selectedLocation, setSelectedLocation] = useState(null);

  const handleLocationChange = (location) => {
    setSelectedLocation(location);
  };

  const handleDateChange = (formattedDate) => {
    setSelectedDate(formattedDate);
  };

  const handleSubmit = () => {
    console.log("Selected Location:", selectedLocation);
    console.log("Selected Date:", selectedDate);
  };

  return (
    <>
      <div className="flex flex-wrap justify-evenly items-center mx-10 sm:flex-row gap-2 sm:gap-0">
        <div className="flex w-[80%] sm:w-[30%]">
          <Input
            type="text"
            placeholder={selectedLocation ? selectedLocation : "Location"}
            className="rounded-tl-2xl rounded-bl-2xl border-r-none border-gray-800 bg-white"
          />
          <DropdownMenuLoc
            roadNames={props.roadNames}
            onLocationChange={handleLocationChange}
          />
        </div>
        <CalendarDemo onDateChange={handleDateChange} />
        <Button
          className="rounded-2xl px-4 py-2 border border-gray-800 bg-white text-black text-sm hover:shadow-[4px_4px_0px_0px_rgba(0,0,0)] transition duration-200"
          onClick={handleSubmit}
        >
          Submit
        </Button>
      </div>
    </>
  );
}
