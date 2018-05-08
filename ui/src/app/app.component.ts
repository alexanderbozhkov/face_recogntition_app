import { Component } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {

  selectedFile: File = null;
  fileName: String = null;

  constructor(private http: HttpClient) {}

  onFileSelected(event){
    this.selectedFile = <File>event.target.files[0];
  }

  onFileNameInput(event){
    console.log('@@@@: ', event.target);
  }

  onUpload(){
    const fd = new FormData();
    fd.append('image_file', this.selectedFile, this.selectedFile.name);
    fd.append('name', this.selectedFile.name);
    console.log('@@: ', this.selectedFile)
    this.http.post('http://localhost:5000/Images/upload', fd).subscribe(res => {
      console.log(res);
    }) // fd - body of the POST request
  }
  
}
