export function Navbar() {
  return (
    <>
      <header className="bg-white border-gray-800 border-b-4 h-20">
        <div className="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
          <div className="flex h-20 items-center justify-between">
            <div className="md:flex md:items-center md:gap-12">
              <a className="block text-gray-400" href="#">
                <span className="sr-only">Home</span>
                <h1 className="flex flex-col font-bold text-gray-800 text-2xl">
                  Smart Traffic Analysis
                </h1>
              </a>
            </div>
          </div>
        </div>
      </header>
    </>
  );
}
