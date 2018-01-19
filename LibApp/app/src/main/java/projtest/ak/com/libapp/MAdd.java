package projtest.ak.com.libapp;

import android.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MAdd extends AppCompatActivity {

    DatabaseHelper db;
    EditText mbook, mborr, mdate;
    Button msave;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_madd);

        db = new DatabaseHelper(this);

        mbook = (EditText) findViewById(R.id.mbook);
        mborr = (EditText) findViewById(R.id.mper);
        mdate = (EditText) findViewById(R.id.mdate);
        mdate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                myDateDialog dialog = new myDateDialog(v);
                FragmentTransaction ft = getFragmentManager().beginTransaction();
                dialog.show(ft, "DatePicker");
            }
        });

        msave = (Button) findViewById(R.id.msave);

        addBorrow();
    }

    public void addBorrow(){
        msave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean isUpdated = db.updateBorr(mbook.getText().toString(), mborr.getText().toString(), mdate.getText().toString());
                if (isUpdated == true)
                    Toast.makeText(MAdd.this, "Data updated", Toast.LENGTH_LONG).show();
                else
                    Toast.makeText(MAdd.this, "Data not updated", Toast.LENGTH_LONG).show();
            }
        });
    }
}
