using System.Collections;
using System.Collections.Generic;
using System.IO.Ports;
using UnityEngine;

public class Ctrl : MonoBehaviour {

    public TextMesh somethings;
    SerialPort stream = new SerialPort("COM7", 38400);


	// Use this for initialization
	void Start () {
        stream.Open();
        
	}
	
	// Update is called once per frame
	void Update () {
        string value = stream.ReadLine();
        somethings.text = value.ToString();
    }
}
