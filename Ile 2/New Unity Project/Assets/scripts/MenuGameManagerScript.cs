using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class MenuGameManagerScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	public void NewGame () {
		SceneManager.LoadScene ("Ile1");
	}

	public void QuitGame () {
		Application.Quit ();
	}
}
