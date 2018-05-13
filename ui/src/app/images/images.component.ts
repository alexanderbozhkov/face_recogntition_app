import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {HttpClient} from '@angular/common/http';
import { forEach } from '@angular/router/src/utils/collection';

@Component({
  selector: 'app-images',
  templateUrl: "./images.component.html",
  styleUrls: ['./images.component.css']
})

export class ImagesComponent implements OnInit {

  constructor(private http: HttpClient, private router: Router) { }

  data: any;
  images: any;
  selectedImage: any;

  selectImage(image){
    this.selectedImage = image;
  }

  deleteImage(image){
    this.http.delete('http://localhost:5000/Images/delete/' + image.image_id).subscribe();
    var index = this.images.findIndex((img) => { 
      return img.image_id == image.image_id;
    });
    this.images.splice(index, 1);
  };

  getAllImages(){
    this.data = this.http.get("http://localhost:5000/Images/all").subscribe(data => {
      console.log('@@@@@', data);
    });

  }

  goBack(){
    this.router.navigate(['/']);
  }

  ngOnInitBackup() {
    this.images = this.http.get("http://localhost:5000/Images/all");
  }

  ngOnInit() {
    
    this.http.get("http://localhost:5000/Images/all").subscribe(data => {
      this.images = data});
  }

}
