import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { IoIosArrowDropdown } from "react-icons/io";

export function DropdownMenuLoc({ roadNames, onLocationChange }) {
  const handleSelect = (roadName) => {
    onLocationChange(roadName); // Notify parent of the selected location
  };
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button
          variant="outline"
          className="rounded-tr-2xl rounded-br-2xl bg-white border border-gray-800 border-l-none text-black text-lg hover:shadow-[4px_4px_0px_0px_rgba(0,0,0)] transition duration-200"
        >
          <IoIosArrowDropdown></IoIosArrowDropdown>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56 bg-white text-black overflow-y-auto max-h-60">
        <DropdownMenuLabel>Menu</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuGroup>
          {roadNames.map((roadName, index) => (
            <DropdownMenuItem
              key={`${roadName}-${index}`}
              onClick={() => handleSelect(roadName)}
              className="hover:shadow-[2px_2px_2px_2px_rgba(0,0,0)] transition duration-200 cursor-pointer"
            >
              <span>{roadName}</span>
            </DropdownMenuItem>
          ))}
        </DropdownMenuGroup>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
