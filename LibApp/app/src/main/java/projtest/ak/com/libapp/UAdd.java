package projtest.ak.com.libapp;

import android.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.format.DateFormat;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.sql.Date;
import java.text.SimpleDateFormat;


public class UAdd extends AppCompatActivity {

    DatabaseHelper db;
    EditText bname, aname;
    Button save;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_uadd);

        db = new DatabaseHelper(this);

        bname = (EditText) findViewById(R.id.addbook);
        aname = (EditText) findViewById(R.id.addauth);
        save = (Button) findViewById(R.id.addsave);
        addData();
    }

    public void addData() {
        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean isInserted = db.insertData(bname.getText().toString(), aname.getText().toString(), null, null);
                if (isInserted == true)
                    Toast.makeText(UAdd.this, "Data inserted", Toast.LENGTH_LONG).show();
                else
                    Toast.makeText(UAdd.this, "Data not inserted", Toast.LENGTH_LONG).show();
            }
        });
    }
}