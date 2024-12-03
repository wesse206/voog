import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormGroup, FormControl, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CommonModule } from '@angular/common';
import { NavigationComponent } from './navigation/navigation.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ReactiveFormsModule, CommonModule, NavigationComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',

})
export class AppComponent {
  title = 'voog';

  Lookup() {
    alert('Clicked!')
  }

  lookupForm = new FormGroup({
    teacherCode: new FormControl(''),
    day: new FormControl(''),
  });

  orphans = null

  onSubmit() {
    console.log(this.lookupForm.value['day'])

    this.getData().subscribe(data => {
      this.orphans = data
      console.log(this.orphans)
    })
  }

  getData(): Observable<any> {
    return this.http.get(`/api/getteacher?TeacherCode=${this.lookupForm.value['teacherCode']}&Day=${this.lookupForm.value['day']}`); // The proxy will forward this to http://localhost:4000/api/data
  }

  constructor(private http: HttpClient) { }

}