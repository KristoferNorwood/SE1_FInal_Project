import 'package:flutter/material.dart';

void main() {
  runApp(Lesson1App());
}

class Lesson1App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Build method is called whenever this widget is displayed
    return MaterialApp(
      home: Text('Lesson1 App'), // Will display this text in the widget
    );
  }
}
