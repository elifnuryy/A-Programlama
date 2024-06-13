using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class SendRequest : MonoBehaviour
{
    public string url = "http://127.0.0.1:5000/predict"; // Flask API URL
    public float x = 17.99f; // Test verisi (de i tirin)
    public float y = 10.38f; // Test verisi (de i tirin)

    void OnMouseDown()
    {
        if (gameObject.CompareTag("red"))
        {
            StartCoroutine(SendPostRequest());
        }
    }

    IEnumerator SendPostRequest()
    {
        // JSON formatında veriyi hazırlama
        string json = JsonUtility.ToJson(new Data() { x = x, y = y });

        // POST isteği hazırlama
        using (UnityWebRequest request = new UnityWebRequest(url, "POST"))
        {
            byte[] bodyRaw = new System.Text.UTF8Encoding().GetBytes(json);
            request.uploadHandler = new UploadHandlerRaw(bodyRaw);
            request.downloadHandler = new DownloadHandlerBuffer();
            request.SetRequestHeader("Content-Type", "application/json");

            // İstek gönderme
            yield return request.SendWebRequest();

            // Yanıtı işleme
            if (request.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError(request.error);
            }
            else
            {
                Debug.Log("Received: " + request.downloadHandler.text);
                ProcessResponse(request.downloadHandler.text);
            }
        }
    }


    void ProcessResponse(string response)
    {
        // Yan t  JSON format nda   zme ve i leme
        ResponseData responseData = JsonUtility.FromJson<ResponseData>(response);
        Debug.Log("Prediction: " + responseData.prediction);
    }

    // JSON verisi i in yard mc  s n f
    [System.Serializable]
    public class Data
    {
        public float x;
        public float y;
    }

    // JSON yan t  i in yard mc  s n f
    [System.Serializable]
    public class ResponseData
    {
        public int prediction;
    }
}
