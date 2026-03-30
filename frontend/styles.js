import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#f2f2f2' },
  header: { marginBottom: 20 },
  title: { fontSize: 28, fontWeight: 'bold', textAlign: 'center', marginBottom: 10 },
  switchContainer: { flexDirection: 'row', justifyContent: 'center', alignItems: 'center' },
  switchLabel: { marginRight: 10, fontSize: 16 },
  input: { height: 50, borderColor: '#ccc', borderWidth: 1, paddingHorizontal: 10, marginBottom: 10, borderRadius: 8, backgroundColor: '#fff' },
  flightCard: { padding: 15, marginVertical: 8, borderRadius: 10, shadowColor: '#000', shadowOpacity: 0.1, shadowRadius: 5, elevation: 2 },
  onTime: { backgroundColor: '#d4edda' },
  delayed: { backgroundColor: '#f8d7da' },
  flightNumber: { fontSize: 18, fontWeight: '600' },
  flightStatus: { fontSize: 16, marginTop: 5 },
  flightInfo: { fontSize: 14, marginTop: 2 },
});

const darkStyles = StyleSheet.create({
  ...styles,
  container: { ...styles.container, backgroundColor: '#121212' },
  input: { ...styles.input, backgroundColor: '#1e1e1e', borderColor: '#444', color: '#fff' },
  title: { ...styles.title, color: '#fff' },
  switchLabel: { ...styles.switchLabel, color: '#fff' },
  flightNumber: { ...styles.flightNumber, color: '#fff' },
  flightStatus: { ...styles.flightStatus, color: '#fff' },
  flightInfo: { ...styles.flightInfo, color: '#fff' },
  onTime: { backgroundColor: '#2e7d32' },
  delayed: { backgroundColor: '#c62828' },
});

export default styles;
export { darkStyles };
