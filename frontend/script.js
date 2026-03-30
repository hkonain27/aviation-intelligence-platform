import React, { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, Switch } from 'react-native';
import styles, { darkStyles } from './styles';

export default function App() {
  const [flightNumber, setFlightNumber] = useState('');
  const [flights, setFlights] = useState([]);
  const [darkMode, setDarkMode] = useState(false);

  const addFlight = () => {
    if (flightNumber.trim() !== '') {
      // Randomly assign delay for demo
      const isDelayed = Math.random() > 0.5;
      const newFlight = {
        id: Math.random().toString(),
        number: flightNumber.toUpperCase(),
        status: isDelayed ? 'Delayed' : 'On Time',
      };
      setFlights([...flights, newFlight]);
      setFlightNumber('');
    }
  };

  const currentStyles = darkMode ? darkStyles : styles;

  return (
    <View style={currentStyles.container}>
      <View style={currentStyles.header}>
        <Text style={currentStyles.title}>✈️ Flight Tracker</Text>
        <View style={currentStyles.switchContainer}>
          <Text style={currentStyles.switchLabel}>{darkMode ? 'Dark Mode' : 'Light Mode'}</Text>
          <Switch value={darkMode} onValueChange={setDarkMode} />
        </View>
      </View>

      <TextInput
        style={currentStyles.input}
        placeholder="Enter Flight Number"
        placeholderTextColor={darkMode ? '#ccc' : '#888'}
        value={flightNumber}
        onChangeText={setFlightNumber}
      />
      <Button title="Add Flight" onPress={addFlight} />

      <FlatList
        data={flights}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View
            style={[
              currentStyles.flightCard,
              item.status === 'On Time' ? currentStyles.onTime : currentStyles.delayed,
            ]}
          >
            <Text style={currentStyles.flightNumber}>{item.number}</Text>
            <Text style={currentStyles.flightStatus}>{item.status}</Text>
          </View>
        )}
      />
    </View>
  );
}
