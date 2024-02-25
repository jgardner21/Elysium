import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import axios from 'axios';

export default function App() {
  const [message, setMessage] = useState('');
  useEffect(() => {
    axios.get('http://localhost:8000/api/hello/')
    .then(response => {
      console.log(response.data.message)
      setMessage(response.data.message);
    }).catch(error => {
      console.log(error);
    });
  }, []);

  return (
    <View style={styles.container}>
      <Text>{message}</Text>
      <Text>Trivial is Working!</Text>
      <Text>Backend message is not :(</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});