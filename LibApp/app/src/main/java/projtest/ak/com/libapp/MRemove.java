package projtest.ak.com.libapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MRemove extends AppCompatActivity {
    DatabaseHelper db;
    EditText rbook;
    Button mrem;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mremove);

        db = new DatabaseHelper(this);

        rbook = (EditText) findViewById(R.id.rbook);
        mrem = (Button) findViewById(R.id.mrem);

        remBorrow();
    }

    public void remBorrow() {
        mrem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean isUpdated = db.updateBorr(rbook.getText().toString(), null, null);
                if (isUpdated == true)
                    Toast.makeText(MRemove.this, "Data updated", Toast.LENGTH_LONG).show();
                else
                    Toast.makeText(MRemove.this, "Data not updated", Toast.LENGTH_LONG).show();
            }
        });
    }
}