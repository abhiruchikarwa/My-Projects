package projtest.ak.com.libapp;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {
    public static final String DBname = "LibDB";
    public static final String TB1 = "Library";
    public static final String col1 = "ID";
    public static final String col2 = "Book";
    public static final String col3 = "Author";
    public static final String col4 = "Borrower";
    public static final String col5 = "DATEOB";

    public DatabaseHelper(Context context) {
        super(context, DBname, null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("create table " + TB1 + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, BOOK TEXT, AUTHOR TEXT, BORROWER TEXT, DATEOB TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS "+ TB1);
        onCreate(db);
    }

    public boolean insertData(String book, String author, String borrower, String date){
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues cv = new ContentValues();
        cv.put(col2, book);
        cv.put(col3, author);
        cv.put(col4, borrower);
        cv.put(col5, date);
        long res = db.insert(TB1, null,cv);
        if(res == -1)
            return false;
        else
            return true;
    }
    public boolean updateBorr(String book, String borrower, String date) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues cv = new ContentValues();
        cv.put(col2, book);
        cv.put(col4, borrower);
        cv.put(col5, date);
        db.update(TB1, cv, "BOOK = ?", new String[]{book});
        return true;
    }

    public Integer removeData(String bname){
        SQLiteDatabase db = this.getWritableDatabase();
        return db.delete(TB1, "BOOK = ?", new String[]{bname});

    }
    public Cursor getAllData(){
        SQLiteDatabase db = this.getWritableDatabase();
        Cursor res = db.rawQuery("SELECT * from "+TB1, null);
        return res;
    }
}