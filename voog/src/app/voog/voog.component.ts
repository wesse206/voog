import { Component } from '@angular/core';
import { ApiService } from '../api.service';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-voog',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './voog.component.html',
  styleUrl: './voog.component.css'
})
export class VoogComponent {
  lookupForm = new FormGroup({
    teacherCode: new FormControl(''),
    day: new FormControl(''),
  });

  voogLearners = null
  onSubmit() {
    let TeacherCode = String(this.lookupForm.value['teacherCode'])
    let Day = Number(this.lookupForm.value['day'])

    this.api.getTeacherlessLearnersVoog(TeacherCode, Day).subscribe(data => {
      this.voogLearners = data
      console.log(data)
    })
  }

  constructor (private api: ApiService) {}
}
