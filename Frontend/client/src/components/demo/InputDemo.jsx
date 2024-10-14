import { Input } from "@/components/ui/input";
import { DropdownMenuLoc } from "./DropdownLoc";
import { CalendarDemo } from "./CalendarDemo";

export function InputDemo() {
  return (
    <>
      <div className="flex flex-col gap-4 sm:flex-row">
        <div className="flex w-[80%] m-auto text-gray-500 rounded-xl sm:w-[30%]">
          <Input type="text" placeholder="Location" />
          <DropdownMenuLoc />
        </div>
        <div className="flex w-[80%] m-auto text-gray-500 rounded-xl sm:w-[30%]">
          <CalendarDemo/>
        </div>
      </div>
    </>
  );
}
