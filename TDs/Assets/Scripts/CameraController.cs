using UnityEngine;
using System.Collections;

public class CameraController : MonoBehaviour {
	public GameObject baseObject;
	public Vector3 offset;

	// Use this for initialization
	void Start () {
		offset = transform.position - baseObject.transform.position;
	}
	
	// Update is called once per frame
	void Update () {
		transform.position = baseObject.transform.position + offset;
	}
}
