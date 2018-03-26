package doge.rfid.rfidplacing;

import android.nfc.NfcAdapter;
import android.nfc.NfcManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        NfcManager manager = (NfcManager) getSystemService(MainActivity.NFC_SERVICE);
        NfcAdapter adapter = null;
        if (manager != null) {
            adapter = manager.getDefaultAdapter();
        }
        if (adapter != null && adapter.isEnabled()) {
            Toast.makeText(this, "NFC is supported", Toast.LENGTH_LONG).show();
            //Yes NFC available
        }else{
            Toast.makeText(this, "NFC is not supported", Toast.LENGTH_LONG).show();
            //Your device doesn't support NFC
        }
    }
}
