import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder } from '@angular/forms';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styles: []
})

export class UploadComponent implements OnInit {

  selectedFile: File = null;
  fileName: string = null;
  form: FormGroup;
  allowClick: boolean = false;
  allowClick2: boolean = false;

  constructor(private formBuilder: FormBuilder, private http: HttpClient, private router: Router) {}

  onFileSelected(event){
    this.selectedFile = <File>event.target.files[0];
    this.allowClick = true;
  }

  onFileNameInput(event){
    this.fileName = <string>event.target.value;
    
  }
  
  onUpload(){
    const fd = new FormData();
    fd.append('image_file', this.selectedFile, this.selectedFile.name);
    fd.append('name', this.fileName);
    this.http.post('http://localhost:5000/Images/upload', fd).subscribe(res => {
      this.allowClick2 = true;
    }) // fd - body of the POST request
  }

  goBack(){
    this.router.navigate(['/']);
  }

  ngOnInit() {
    
  }

}
