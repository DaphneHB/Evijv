using UnityEngine;
using System.Collections;

public class BallController : MonoBehaviour {
	public int speed = 2;
	public Rigidbody rb;
	// Use this for initialization
	void Start () {
		rb = GetComponent<Rigidbody> ();
	}
	
	// Update is called once per frame
	void Update () {
		KeyboardMovements ();
	}

	void KeyboardMovements () {
		if (Input.GetKey ("right")) {
			rb.AddForce (Vector3.right * speed);
		} else if (Input.GetKey ("left")) {
			rb.AddForce (Vector3.left * speed);
		} else if (Input.GetKey ("up")) {
			rb.AddForce (Vector3.forward * speed);
		} else if (Input.GetKey ("down")) {
			rb.AddForce (Vector3.back * speed);
		}
	}
}
