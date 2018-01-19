package projtest.ak.com.libapp;

import android.app.AlertDialog;
import android.content.Intent;
import android.database.Cursor;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class Manage extends AppCompatActivity {

    Button madd, mrem, mview;
    DatabaseHelper db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_manage);

        db= new DatabaseHelper(this);
        madd = (Button) findViewById(R.id.mbn1);
        mrem = (Button) findViewById(R.id.mbn2);
        mview = (Button) findViewById(R.id.mbn3);

        madd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(Manage.this, MAdd.class));
            }
        });

        mrem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(Manage.this, MRemove.class));
            }
        });

        mview.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewAll();
            }
        });
    }

    public void viewAll(){
        Cursor res = db.getAllData();
        if(res.getCount() == 0){
            Toast.makeText(Manage.this, "No Data", Toast.LENGTH_LONG).show();
        }
        StringBuffer buffer = new StringBuffer();
        while (res.moveToNext()){
            buffer.append("\nBook ID:"+res.getString(0)+"\n");
            buffer.append("Book:"+res.getString(1)+"\n");
            buffer.append("Borrowed by:"+res.getString(3)+"\n");
            buffer.append("Borrowed on:"+res.getString(4)+"\n");

        }
        showMessage("Data", buffer.toString());
    }

    public void showMessage(String title, String Message){
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setTitle(title);
        builder.setMessage(Message);
        builder.show();
    }
}