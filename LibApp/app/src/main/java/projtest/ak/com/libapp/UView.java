package projtest.ak.com.libapp;

import android.app.AlertDialog;
import android.database.Cursor;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

public class UView extends AppCompatActivity {

    DatabaseHelper db;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_uview);

        db = new DatabaseHelper(this);
        viewAll();
        }
    public void viewAll(){
        Cursor res = db.getAllData();
        if(res.getCount() == 0){
            Toast.makeText(UView.this, "No Data", Toast.LENGTH_LONG).show();
        }
        StringBuffer buffer = new StringBuffer();
        while (res.moveToNext()){
            buffer.append("Number:"+res.getString(0)+"\n");
            buffer.append("Book:"+res.getString(1)+"\n");
            buffer.append("Author:"+res.getString(2)+"\n");
            buffer.append("Borrowed by:"+res.getString(3)+"\n");
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
