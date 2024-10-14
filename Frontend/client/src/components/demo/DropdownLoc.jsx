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

export function DropdownMenuLoc() {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline">
          <IoIosArrowDropdown className="text-black txt-xl"></IoIosArrowDropdown>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56 bg-gray-500 text-white">
        <DropdownMenuLabel>Menu</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuGroup>
          <DropdownMenuItem>
            <span>Andheri</span>
          </DropdownMenuItem>

          <DropdownMenuItem>
            <span>Virar</span>
          </DropdownMenuItem>

          <DropdownMenuItem>
            <span>Mumbai</span>
          </DropdownMenuItem>

          <DropdownMenuItem>
            <span>Kanjurmarg </span>
          </DropdownMenuItem>
        </DropdownMenuGroup>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
