import { Component, OnInit} from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit{

  form: FormGroup;

  constructor(private formBuilder: FormBuilder, private http: HttpClient) {}


  ngOnInit() {
    this.form = this.formBuilder.group({
      validName: [null, [Validators.required]],
      validUpload: [null, [Validators]]
    });
  }
}
