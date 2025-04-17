// App.js
import React, { useEffect, useState } from 'react';
import { Text, View, FlatList, Platform, StyleSheet } from 'react-native';
import * as Notifications from 'expo-notifications';
import Constants from 'expo-constants';
import io from 'socket.io-client';

export default function App() {
  type Message = {
    id: string;
    title: string;
    message: string;
  };
  
  const [messages, setMessages] = useState<Message[]>([]);  
  const [expoPushToken, setExpoPushToken] = useState<string | null>(null);


  useEffect(() => {
    registerForPushNotificationsAsync().then((token: string | undefined) => {
      if (token) {
        setExpoPushToken(token);
        console.log("Expo Push Token:", token);
      }
    });
    const socket = io("http://192.168.137.1:5000"); // Replace with actual IP
    socket.on('notification', (data) => {
      setMessages(prev => [{ id: Date.now().toString(), ...data }, ...prev]);

      if (Platform.OS !== 'web') {
        Notifications.scheduleNotificationAsync({
          content: { title: data.title, body: data.message },
          trigger: null,
        });
      }
    });
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>📳 Local Notifier</Text>
      <Text>Push Token: {expoPushToken}</Text>
      <FlatList
        data={messages}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Text style={styles.item}>{item.title}: {item.message}</Text>
        )}
      />
    </View>
  );
}

async function registerForPushNotificationsAsync() {
  const { status: existingStatus } = await Notifications.getPermissionsAsync();
  let finalStatus = existingStatus;

  if (existingStatus !== 'granted') {
    const { status } = await Notifications.requestPermissionsAsync();
    finalStatus = status;
  }

  if (finalStatus !== 'granted') {
    alert('Failed to get push token');
    return;
  }

  const token = (await Notifications.getExpoPushTokenAsync()).data;
  return token;
}

const styles = StyleSheet.create({
  container: { flex: 1, paddingTop: 50, paddingHorizontal: 20 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  item: { marginVertical: 5 }
});
