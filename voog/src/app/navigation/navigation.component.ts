import { Component, Output, EventEmitter, OnDestroy } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ApiService } from '../api.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-navigation',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './navigation.component.html',
  styleUrl: './navigation.component.css'
})
export class NavigationComponent implements OnDestroy {
  TeacherCode: string = '';
  TeacherCodeSubsription: Subscription  

  onSelect(OnderwyserKode: string) {
    this.api.TeacherCode(OnderwyserKode);
  }

  ngOnDestroy() {
    this.TeacherCodeSubsription.unsubscribe()  
  }

  constructor (private api: ApiService) {
    this.TeacherCodeSubsription = api.TeacherCodeSource$.subscribe(
      TeacherCode => {
        this.TeacherCode = TeacherCode
      }
    )
  }

}

