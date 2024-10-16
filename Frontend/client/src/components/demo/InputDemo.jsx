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
      <div className="flex flex-col gap-16 bg-gray-800 rounded-3xl py-20 shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]">
        <div className="flex flex-col text-center">
          <span className="font-bold text-4xl text-center text-white">
            Enter Your{" "}
            <span className="bg-gradient-to-bl from-blue-500 to-blue-800 bg-clip-text text-transparent">
              Route,
            </span>
          </span>
          <span className="font-bold text-6xl text-center text-white">
            <span className="bg-gradient-to-bl from-blue-500 to-blue-800 bg-clip-text text-transparent">
              Predict
            </span>{" "}
            the Future
          </span>
        </div>

        <div className="flex flex-wrap justify-evenly items-center sm:flex-row gap-2 sm:gap-4">
          <div className="flex w-[80%] sm:w-[40%]">
            <Input
              type="text"
              placeholder={
                selectedLocation ? selectedLocation : "Select Location"
              }
              className="rounded-tl-2xl rounded-bl-2xl text-gray-600 bg-white shadow-[0_3px_10px_rgb(0,0,0,0.2)] border border-gray-200"
            />
            <DropdownMenuLoc
              roadNames={props.roadNames}
              onLocationChange={handleLocationChange}
            />
          </div>
          <CalendarDemo onDateChange={handleDateChange} />
          <Button
            className="rounded-2xl px-4 py-2 bg-white hover:bg-gray-800 text-gray-800 hover:text-white text-sm border border-gray-200 sshadow-[rgba(0,_0,_0,_0.4)_0px_30px_90px]"
            onClick={handleSubmit}
          >
            Predict
          </Button>
        </div>
      </div>
    </>
  );
}
