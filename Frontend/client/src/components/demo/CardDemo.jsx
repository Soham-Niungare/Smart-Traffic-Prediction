export function CardDemo() {
  return (
    <>
      <a
        href="#"
        className="block rounded-lg p-4 shadow-sm shadow-indigo-100 border border-gray-200"
      >
        <div className="mt-2">
          <dl>
            <div>
              <dt className="sr-only">Price</dt>

              <dd className="text-sm text-gray-500">$240,000</dd>
            </div>

            <div>
              <dt className="sr-only">Address</dt>

              <dd className="font-medium">123 Wallaby Avenue, Park Road</dd>
            </div>
          </dl>
        </div>
      </a>
    </>
  );
}
