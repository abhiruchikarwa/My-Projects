package projtest.ak.com.libapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class URemove extends AppCompatActivity {
    DatabaseHelper db;
    EditText rbname;
    Button rem;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_uremove);

        db = new DatabaseHelper(this);

        rbname = (EditText) findViewById(R.id.rembook);
        rem = (Button) findViewById(R.id.remsave);
        remData();

    }
    public void remData() {
        rem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Integer deletedrows = db.removeData(rbname.getText().toString());
                if (deletedrows >0)
                    Toast.makeText(URemove.this, "Data deleted", Toast.LENGTH_LONG).show();
                else
                    Toast.makeText(URemove.this, "Data not deleted", Toast.LENGTH_LONG).show();
            }
        });
    }
}
