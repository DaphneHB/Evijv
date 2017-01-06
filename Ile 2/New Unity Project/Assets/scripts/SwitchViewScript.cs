using UnityEngine;
using System.Collections;

public class SwitchViewScript : MonoBehaviour {

	public Camera cam1;
	public Camera cam2;
	bool cam;


	// Use this for initialization
	void Start () {
		cam = true;
		cam1.enabled = true;
		cam2.enabled = false;
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown("v")) {
//			cam = !cam;
			cam1.enabled =!cam1.enabled;
			cam2.enabled =!cam2.enabled;
		}
	}
}
