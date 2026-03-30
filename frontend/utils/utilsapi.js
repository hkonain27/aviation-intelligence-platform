const API_KEY = ''; // (Needs the Api's key)

export async function fetchFlightData(flightNumber) {
  try {
    const response = await fetch(`http://api.aviationstack.com/v1/flights?access_key=${API_KEY}&flight_iata=${flightNumber}`); // ADD API KEY
    const data = await response.json();
    const flightData = data.data?.[0];

    if (!flightData) return null;

    return {
      id: Math.random().toString(),
      number: flightNumber.toUpperCase(),
      status: flightData.flight_status ? flightData.flight_status.charAt(0).toUpperCase() + flightData.flight_status.slice(1) : 'Unknown',
      departure: flightData.departure?.airport || 'N/A',
      arrival: flightData.arrival?.airport || 'N/A',
      scheduled: flightData.departure?.scheduled || 'N/A',
    };
  } catch (error) {
    console.error(error);
    return null;
  }
}
